
% Facts: Fruits and their colors

fruit(apple).
fruit(banana).
fruit(orange).
fruit(grapes).
fruit(mango).

color(apple, red).
color(banana, yellow).
color(orange, orange).
color(grapes, green).
color(mango, yellow).

% Rule to find fruit and its color
fruit_color(Fruit, Color) :-
    fruit(Fruit),
    color(Fruit, Color).

% Display all fruits and their colors
display :-
    fruit_color(Fruit, Color),
    write(Fruit),
    write(' - '),
    write(Color),
    nl,
    fail.

display.
