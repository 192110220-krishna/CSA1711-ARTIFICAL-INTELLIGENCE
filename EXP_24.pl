greatest(A, B, A) :-
    A >= B.

greatest(A, B, B) :-
    B > A.

main :-
    greatest(10, 20, Result),
    write('Greatest number: '),
    writeln(Result),
    halt.

:- initialization(main).
