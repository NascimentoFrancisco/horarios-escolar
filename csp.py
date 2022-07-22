"""CSP (Constraint Satisfaction Problems) problems and solvers. (Chapter 6)."""

from utils import argmin_random_tie, count, first
import search

from collections import defaultdict
from functools import reduce

import itertools
import re
import random


class CSP(search.Problem):
    """Esta classe descreve problemas de satisfação de restrições de domínio finito.
    Um CSP é especificado pelas seguintes entradas:
        variáveis ​​Uma lista de variáveis; cada um é atômico (por exemplo, int ou string).
        domínios Um dict de {var:[possible_value, ...]} entradas.
        vizinhos Um ditado de {var:[var,...]} que para cada variável lista
                    as outras variáveis ​​que participam das restrições.
        restrições Uma função f(A, a, B, b) que retorna true se vizinhos
                    A, B satisfazem a restrição quando possuem valores A=a, B=b
    No livro-texto e na maioria das definições matemáticas, o
    restrições são especificadas como pares explícitos de valores permitidos,
    mas a formulação aqui é mais fácil de expressar e mais compacta para
    maioria dos casos. (Por exemplo, o problema das n-rainhas pode ser representado
    no espaço O(n) usando esta notação, em vez de O(N^4) para o
    representação explícita.) Em termos de descrever o CSP como um
    problema, isso é tudo que existe.
    No entanto, a classe também suporta estruturas de dados e métodos que ajudam você
    resolver CSPs chamando uma função de pesquisa no CSP. Métodos e slots são
    como segue, onde o argumento 'a' representa uma atribuição, que é uma
    dict de {var:val} entradas:
        assign(var, val, a) Atribua a[var] = val; fazer outra contabilidade
        unassign(var, a) Do del a[var], além de outras escriturações
        nconflicts(var, val, a) Retorna o número de outras variáveis ​​que
                                conflito com var=val
        curr_domains[var] Slot: valores consistentes restantes para var
                                Usado por rotinas de propagação de restrição.
    Os métodos a seguir são usados ​​apenas por graph_search e tree_search:
        actions(state) Retorna uma lista de ações
        resultado(estado, ação) Retorna um sucessor de estado
        goal_test(state) Retorna true se todas as restrições forem satisfeitas
    Os seguintes são apenas para fins de depuração:
        nassigns Slot: rastreia o número de atribuições feitas
        display(a) Imprime uma representação legível por humanos
    """

    def __init__(self, variables, domains, neighbors, constraints):
        """Construa um problema CSP. Se as variáveis ​​estiverem vazias, ele se tornará domains.keys()."""
        variables = variables or list(domains.keys())

        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.initial = ()
        self.curr_domains = None
        self.nassigns = 0

    def assign(self, var, val, assignment):
        """Adicione {var: val} à atribuição; Descarte o valor antigo, se houver."""
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        """Remova {var: val} da atribuição.
        NÃO chame isso se você estiver alterando uma variável para um novo valor;
        basta chamar assign para isso."""
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
        """Retorna o número de conflitos que var=val tem com outras variáveis."""
        # As subclasses podem implementar isso de forma mais eficiente
        def conflict(var2):
            return (var2 in assignment and
                    not self.constraints(var, val, var2, assignment[var2]))
        return count(conflict(v) for v in self.neighbors[var])

    def display(self, assignment):
        """Mostre uma representação legível do CSP."""
        # As subclasses podem imprimir de uma maneira mais bonita ou exibir com uma GUI
        print('CSP:', self, 'with assignment:', assignment)

    # Esses métodos são para a interface de busca em árvore e gráfico:

    def actions(self, state):
        """Retornar uma lista de ações aplicáveis: não conflitantes
        atribuições para uma variável não atribuída."""
        if len(state) == len(self.variables):
            return []
        else:
            assignment = dict(state)
            var = first([v for v in self.variables if v not in assignment])
            return [(var, val) for val in self.domains[var]
                    if self.nconflicts(var, val, assignment) == 0]

    def result(self, state, action):
        """Execute uma ação e retorne o novo estado."""
        (var, val) = action
        return state + ((var, val),)

    def goal_test(self, state):
        """O objetivo é atribuir todas as variáveis, com todas as restrições satisfeitas."""
        assignment = dict(state)
        return (len(assignment) == len(self.variables)
                and all(self.nconflicts(variables, assignment[variables], assignment) == 0
                        for variables in self.variables))

    # Estes são para propagação de restrição

    def support_pruning(self):
        """Certifique-se de que podemos remover valores de domínios. (Queremos pagar
        para isso apenas se o usarmos.)"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def suppose(self, var, value):
        """Comece a acumular inferências assumindo var=value."""
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        self.curr_domains[var] = [value]
        return removals

    def prune(self, var, value, removals):
        """Descarte var=valor."""
        self.curr_domains[var].remove(value)
        if removals is not None:
            removals.append((var, value))

    def choices(self, var):
        """Retorna todos os valores para var que não estão descartados no momento."""
        return (self.curr_domains or self.domains)[var]

    def infer_assignment(self):
        """Retorne a atribuição parcial implícita pelas inferências atuais."""
        self.support_pruning()
        return {v: self.curr_domains[v][0]
                for v in self.variables if 1 == len(self.curr_domains[v])}

    def restore(self, removals):
        """Desfaça uma suposição e todas as inferências dela."""
        for B, b in removals:
            self.curr_domains[B].append(b)

    # Isto é para pesquisa min_conflicts

    def conflicted_vars(self, current):
        """Retorna uma lista de variáveis ​​na atribuição atual que estão em conflito"""
        return [var for var in self.variables
                if self.nconflicts(var, current[var], current) > 0]

# ______________________________________________________________________________
# Propagação de restrição com AC-3


def AC3(csp, queue=None, removals=None):
    """[Figure 6.3]"""
    if queue is None:
        queue = [(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]]
    csp.support_pruning()
    while queue:
        (Xi, Xj) = queue.pop()
        if revise(csp, Xi, Xj, removals):
            if not csp.curr_domains[Xi]:
                return False
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True


def revise(csp, Xi, Xj, removals):
    """Retorna true se removermos um valor."""
    revised = False
    for x in csp.curr_domains[Xi][:]:
        # Se Xi=x entrar em conflito com Xj=y para todo y possível, elimine Xi=x
        if all(not csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
            csp.prune(Xi, x, removals)
            revised = True
    return revised

# ______________________________________________________________________________
# Pesquisa de retorno de CSP

# Ordem variável


def first_unassigned_variable(assignment, csp):
    """A ordem da variável padrão."""
    return first([var for var in csp.variables if var not in assignment])


def mrv(assignment, csp):
    """Heurística de valores mínimos restantes."""
    return argmin_random_tie(
        [v for v in csp.variables if v not in assignment],
        key=lambda var: num_legal_values(csp, var, assignment))


def num_legal_values(csp, var, assignment):
    if csp.curr_domains:
        return len(csp.curr_domains[var])
    else:
        return count(csp.nconflicts(var, val, assignment) == 0
                     for val in csp.domains[var])

# Ordem de valor


def unordered_domain_values(var, assignment, csp):
    """A ordem de valor padrão."""
    return csp.choices(var)


def lcv(var, assignment, csp):
    """Heurística de valores mínimos."""
    return sorted(csp.choices(var),
                  key=lambda val: csp.nconflicts(var, val, assignment))

# Inference


def no_inference(csp, var, value, assignment, removals):
    return True


def forward_checking(csp, var, value, assignment, removals):
    """Podar valores vizinhos inconsistentes com var=value."""
    csp.support_pruning()
    for B in csp.neighbors[var]:
        if B not in assignment:
            for b in csp.curr_domains[B][:]:
                if not csp.constraints(var, value, B, b):
                    csp.prune(B, b, removals)
            if not csp.curr_domains[B]:
                return False
    return True


def mac(csp, var, value, assignment, removals):
    """Mantenha a consistência do arco."""
    return AC3(csp, [(X, var) for X in csp.neighbors[var]], removals)

# The search, proper


def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """[Figure 6.5]"""

    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment
        var = select_unassigned_variable(assignment, csp)
        for value in order_domain_values(var, assignment, csp):
            if 0 == csp.nconflicts(var, value, assignment):
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value)
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result is not None:
                        return result
                csp.restore(removals)
        csp.unassign(var, assignment)
        return None

    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result

# ______________________________________________________________________________
#Pesquisa de escalada de conflitos mínimos para CSPs


def min_conflicts(csp, max_steps=100000):
    """Resolva um CSP fazendo uma escalada estocástica no número de conflitos."""
    # Gera uma atribuição completa para todas as variáveis ​​(provavelmente com conflitos)
    csp.current = current = {}
    for var in csp.variables:
        val = min_conflicts_value(csp, var, current)
        csp.assign(var, val, current)
    # Agora escolha repetidamente uma variável aleatória em conflito e altere-a
    for i in range(max_steps):
        conflicted = csp.conflicted_vars(current)
        if not conflicted:
            return current
        var = random.choice(conflicted)
        val = min_conflicts_value(csp, var, current)
        csp.assign(var, val, current)
    return None


def min_conflicts_value(csp, var, current):
    """Retorna o valor que dará a var o menor número de conflitos.
    Se houver empate, escolha aleatoriamente."""
    return argmin_random_tie(csp.domains[var],
                             key=lambda val: csp.nconflicts(var, val, current))

# ______________________________________________________________________________


def tree_csp_solver(csp):
    """[Figure 6.11]"""
    assignment = {}
    root = csp.variables[0]
    X, parent = topological_sort(csp, root)

    csp.support_pruning()
    for Xj in reversed(X[1:]):
        if not make_arc_consistent(parent[Xj], Xj, csp):
            return None

    assignment[root] = csp.curr_domains[root][0]
    for Xi in X[1:]:
        assignment[Xi] = assign_value(parent[Xi], Xi, csp, assignment)
        if not assignment[Xi]:
            return None
    return assignment


def topological_sort(X, root):
    """Retorna o tipo topológico de X a partir da raiz.
    Entrada:
    X é uma lista com os nós do gráfico
    N é o dicionário com os vizinhos de cada nó
    root denota a raiz do gráfico.
    Resultado:
    pilha é uma lista com os nós ordenados topologicamente
    pais é um dicionário apontando para o pai de cada nó
    Outro:
    visitado mostra o estado (visitado - não visitado) dos nós
    """
    neighbors = X.neighbors

    visited = defaultdict(lambda: False)

    stack = []
    parents = {}

    build_topological(root, None, neighbors, visited, stack, parents)
    return stack, parents


def build_topological(node, parent, neighbors, visited, stack, parents):
    """Construa a ordenação topológica e os pais de cada nó no grafo."""
    visited[node] = True

    for n in neighbors[node]:
        if(not visited[n]):
            build_topological(n, node, neighbors, visited, stack, parents)

    parents[node] = parent
    stack.insert(0, node)


def make_arc_consistent(Xj, Xk, csp):
    """Faça o arco entre pai (Xj) e filho (Xk) consistente sob as restrições do csp,
    removendo os possíveis valores de Xj que causam inconsistências."""
    #csp.curr_domains[Xj] = []
    for val1 in csp.domains[Xj]:
        keep = False # Manter ou remover val1
        for val2 in csp.domains[Xk]:
            if csp.constraints(Xj, val1, Xk, val2):
                # Encontrou uma atribuição consistente para val1, mantenha-a
                keep = True
                break
        
        if not keep:
            # Remova val1
            csp.prune(Xj, val1, None)

    return csp.curr_domains[Xj]


def assign_value(Xj, Xk, csp, assignment):
    """Atribua um valor a Xk dada a atribuição de Xj (pai de Xk).
    Retorne o primeiro valor que satisfaça as restrições."""
    parent_assignment = assignment[Xj]
    for val in csp.curr_domains[Xk]:
        if csp.constraints(Xj, parent_assignment, Xk, val):
            return val

    # Nenhuma atribuição consistente disponível
    return None