
% Facts
male(john).
male(paul).
male(mike).

female(mary).
female(lisa).

parent(john, paul).
parent(mary, paul).
parent(john, lisa).
parent(mary, lisa).
parent(paul, mike).

% Rules
father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

child(X, Y) :-
    parent(Y, X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
