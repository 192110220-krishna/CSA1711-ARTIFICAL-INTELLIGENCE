
% Program 27: Best First Search

edge(a,b).
edge(a,c).
edge(b,d).
edge(b,e).
edge(c,f).
edge(c,g).
edge(d,h).
edge(e,g).
edge(f,g).

heuristic(a,6).
heuristic(b,4).
heuristic(c,3).
heuristic(d,5).
heuristic(e,2).
heuristic(f,2).
heuristic(g,0).
heuristic(h,6).

best_first(Start, Goal, Path) :-
    bfs([Start], Goal, [Start], RevPath),
    reverse(RevPath, Path).

bfs([Goal|_], Goal, _, [Goal]).

bfs([Current|Rest], Goal, Visited, Path) :-
    findall(H-Next,
        (edge(Current,Next),
         \+ member(Next,Visited),
         heuristic(Next,H)),
        Children),
    keysort(Children,Sorted),
    extract(Sorted,Nodes),
    append(Rest,Nodes,Queue),
    bfs(Queue,Goal,Visited,Path).

extract([],[]).
extract([_-X|T],[X|R]) :-
    extract(T,R).
