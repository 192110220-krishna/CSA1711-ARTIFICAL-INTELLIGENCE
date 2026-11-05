main :-
    List = [10, 20, 30, 40, 50],

    write('List: '),
    writeln(List),

    List = [First|_],
    write('First Element: '),
    writeln(First),

    last(List, Last),
    write('Last Element: '),
    writeln(Last),

    length(List, Length),
    write('List Length: '),
    writeln(Length),

    halt.

:- initialization(main).
