
% Program 27: Best First Search Algorithm

% Graph connections
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).
edge(d, h).
edge(e, g).
edge(f, g).

% Heuristic values
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 3).
heuristic(d, 5).
heuristic(e, 2).
heuristic(f, 2).
heuristic(g, 0).
heuristic(h, 6).

% Best First Search
best_first(Start, Goal, Path) :-
    search([Start], Goal, [], RevPath),
    reverse(RevPath, Path).

search([Goal|_], Goal, _, [Goal]).

search([Current|Rest], Goal, Visited, [Current|Path]) :-
    findall(H-Next,
        (edge(Current, Next),
         \+ member(Next, Visited),
         \+ member(Next, [Current|Rest]),
         heuristic(Next, H)),
        Children),
    append(Rest, Children, Combined),
    sort(Combined, Sorted),
    extract_nodes(Sorted, NewQueue),
    search(NewQueue, Goal, [Current|Visited], Path).

extract_nodes([], []).
extract_nodes([_-Node|Rest], [Node|Nodes]) :-
    extract_nodes(Rest, Nodes).
