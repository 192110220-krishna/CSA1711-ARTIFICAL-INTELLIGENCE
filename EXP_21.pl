hanoi(1, From, _, To) :-
    write('Move disk from '),
    write(From),
    write(' to '),
    writeln(To).

hanoi(N, From, Aux, To) :-
    N > 1,
    M is N - 1,
    hanoi(M, From, To, Aux),
    hanoi(1, From, Aux, To),
    hanoi(M, Aux, From, To).

main :-
    hanoi(3, left, middle, right),
    halt.

:- initialization(main).
