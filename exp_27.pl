
% Best First Search Algorithm

% Graph connections
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(d, g).
edge(e, g).
edge(f, g).

% Heuristic values
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 2).
heuristic(d, 3).
heuristic(e, 1).
heuristic(f, 1).
heuristic(g, 0).

% Best First Search
best_first(Start, Goal, Path) :-
    heuristic(Start, H),
    search([H-[Start]], Goal, RevPath),
    reverse(RevPath, Path).

% Goal checking
search([_- [Goal|Rest]|_], Goal, [Goal|Rest]).

% Expanding nodes
search([_- [Current|Rest]|Queue], Goal, Path) :-
    findall(H-[Next,Current|Rest],
        (edge(Current, Next),
         \+ member(Next, [Current|Rest]),
         heuristic(Next, H)),
        Children),
    append(Queue, Children, NewQueue),
    keysort(NewQueue, SortedQueue),
    search(SortedQueue, Goal, Path).

% Main program
run :-
    best_first(a, g, Path),
    write('Best First Search Path: '),
    write(Path),
    nl.
