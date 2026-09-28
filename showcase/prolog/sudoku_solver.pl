%%% Dominik Schwagerl, 1. Semester, Symbolische Künstliche Intelligenz %%%


			%%%%% Sudoku Solver %%%%%


:- use_module(library(clpfd)).


%%%% 4x4 Sudoku

sudoku4x4(Puzzle, Solution) :- 
Solution = Puzzle,
Puzzle = [[X11,X12,X13,X14],[X21,X22,X23,X24],[X31,X32,X33,X34],[X41,X42,X43,X44]],

%%% Check if Rows / Columns / Squares are a Permutation of 1, 2, 3, 4 (so all the four numbers only appear once)
% Rows
permutation([X11,X12,X13,X14],[1,2,3,4]), permutation([X21,X22,X23,X24],[1,2,3,4]), permutation([X31,X32,X33,X34],[1,2,3,4]), permutation([X41,X42,X43,X44],[1,2,3,4]), 

% Column
permutation([X11,X21,X31,X41],[1,2,3,4]), permutation([X12,X22,X32,X42],[1,2,3,4]), permutation([X13,X23,X33,X43],[1,2,3,4]), permutation([X14,X24,X34,X44],[1,2,3,4]), 

% Squares
permutation([X11,X12,X21,X22],[1,2,3,4]), permutation([X13,X14,X23,X24],[1,2,3,4]), permutation([X31,X32,X41,X42],[1,2,3,4]), permutation([X33,X34,X43,X44],[1,2,3,4]).


%%%% 6x6 Sudoku

sudoku6x6(Puzzle, Solution) :-
Solution = Puzzle,
Puzzle = [X11,X12,X13,X14,X15,X16,X21,X22,X23,X24,X25,X26,X31,X32,X33,X34,X35,X36,X41,X42,X43,X44,X45,X46,X51,X52,X53,X54,X55,X56,X61,X62,X63,X64,X65,X66],


%% Constraint that all possible Values are between 1 and 6
Solution ins 1 .. 6,

%%% Check if Rows / Cols / Squares have each Value only once, using constraint logic programming for better performance

% Rows
all_distinct([X11,X12,X13,X14,X15,X16]), 
all_distinct([X21,X22,X23,X24,X25,X26]), 
all_distinct([X31,X32,X33,X34,X35,X36]), 
all_distinct([X41,X42,X43,X44,X45,X46]), 
all_distinct([X51,X52,X53,X54,X55,X56]), 
all_distinct([X61,X62,X63,X64,X65,X66]),

% Columns
all_distinct([X11,X21,X31,X41,X51,X61]), 
all_distinct([X12,X22,X32,X42,X52,X62]), 
all_distinct([X13,X23,X33,X43,X53,X63]), 
all_distinct([X14,X24,X34,X44,X54,X64]), 
all_distinct([X15,X25,X35,X45,X55,X65]), 
all_distinct([X16,X26,X36,X46,X56,X66]),

% Rectangle
all_distinct([X11,X12,X13,X21,X22,X23]), 
all_distinct([X14,X15,X16,X24,X25,X26]), 
all_distinct([X31,X32,X33,X41,X42,X43]), 
all_distinct([X34,X35,X36,X44,X45,X46]), 
all_distinct([X51,X52,X53,X61,X62,X63]), 
all_distinct([X54,X55,X56,X64,X65,X66]),

%% output in sudoku shape
pretty_print([[X11,X12,X13,X14,X15,X16],[X21,X22,X23,X24,X25,X26],[X31,X32,X33,X34,X35,X36],[X41,X42,X43,X44,X45,X46],[X51,X52,X53,X54,X55,X56],[X61,X62,X63,X64,X65,X66]]).

sudoku9x9(Puzzle, Solution) :-
Solution = Puzzle,
Puzzle = [X11,X12,X13,X14,X15,X16,X17,X18,X19,
X21,X22,X23,X24,X25,X26,X27,X28,X29,
X31,X32,X33,X34,X35,X36,X37,X38,X39,
X41,X42,X43,X44,X45,X46,X47,X48,X49,
X51,X52,X53,X54,X55,X56,X57,X58,X59,
X61,X62,X63,X64,X65,X66,X67,X68,X69,
X71,X72,X73,X74,X75,X76,X77,X78,X79,
X81,X82,X83,X84,X85,X86,X87,X88,X89,
X91,X92,X93,X94,X95,X96,X97,X98,X99],


%% Constraint that all possible Values are between 1 and 9
Solution ins 1 .. 9,

%%% Check if Rows / Cols / Squares have each Value only once, using constraint logic programming for better performance

% Rows
all_distinct([X11,X12,X13,X14,X15,X16,X17,X18,X19]), 
all_distinct([X21,X22,X23,X24,X25,X26,X27,X28,X29]), 
all_distinct([X31,X32,X33,X34,X35,X36,X37,X38,X39]), 
all_distinct([X41,X42,X43,X44,X45,X46,X47,X48,X49]), 
all_distinct([X51,X52,X53,X54,X55,X56,X57,X58,X59]), 
all_distinct([X61,X62,X63,X64,X65,X66,X67,X68,X69]),
all_distinct([X71,X72,X73,X74,X75,X76,X77,X78,X79]),
all_distinct([X81,X82,X83,X84,X85,X86,X87,X88,X89]),
all_distinct([X91,X92,X93,X94,X95,X96,X97,X98,X99]),

% Columns
all_distinct([X11,X21,X31,X41,X51,X61,X71,X81,X91]), 
all_distinct([X12,X22,X32,X42,X52,X62,X72,X82,X92]), 
all_distinct([X13,X23,X33,X43,X53,X63,X73,X83,X93]), 
all_distinct([X14,X24,X34,X44,X54,X64,X74,X84,X94]), 
all_distinct([X15,X25,X35,X45,X55,X65,X75,X85,X95]), 
all_distinct([X16,X26,X36,X46,X56,X66,X76,X86,X96]),
all_distinct([X17,X27,X37,X47,X57,X67,X77,X87,X97]),
all_distinct([X18,X28,X38,X48,X58,X68,X78,X88,X98]),
all_distinct([X19,X29,X39,X49,X59,X69,X79,X89,X99]),


% Squares
all_distinct([X11,X12,X13,X21,X22,X23,X31,X32,X33]), 
all_distinct([X14,X15,X16,X24,X25,X26,X34,X35,X36]), 
all_distinct([X17,X18,X19,X27,X28,X29,X37,X38,X39]), 
all_distinct([X41,X42,X43,X51,X52,X53,X61,X62,X63]), 
all_distinct([X44,X45,X46,X54,X55,X56,X64,X65,X66]), 
all_distinct([X47,X48,X49,X57,X58,X59,X67,X68,X69]),
all_distinct([X71,X72,X73,X81,X82,X83,X91,X92,X93]),
all_distinct([X74,X75,X76,X84,X85,X86,X94,X95,X96]),
all_distinct([X77,X78,X79,X87,X88,X89,X97,X98,X99]),

%% output in sudoku shape
pretty_print([[X11,X12,X13,X14,X15,X16,X17,X18,X19],
[X21,X22,X23,X24,X25,X26,X27,X28,X29],
[X31,X32,X33,X34,X35,X36,X37,X38,X39],
[X41,X42,X43,X44,X45,X46,X47,X48,X49],
[X51,X52,X53,X54,X55,X56,X57,X58,X59],
[X61,X62,X63,X64,X65,X66,X67,X68,X69],
[X71,X72,X73,X74,X75,X76,X77,X78,X79],
[X81,X82,X83,X84,X85,X86,X87,X88,X89],
[X91,X92,X93,X94,X95,X96,X97,X98,X99]]).

%% print each row in a new line
pretty_print([Head | Tail]) :-
 print(Head),
 nl,
 pretty_print(Tail).




%%%%% Example command lines %%%%%

%%% solves 4x4 sudoku, values can be changed, '_' as placeholder
%% examples
% sudoku4x4([[_,_,4,3],[_,_,_,_],[4,3,_,2],[_,2,_,4]],S).
% sudoku4x4([[_,_,_,_],[1,_,3,_],[4,3,1,_],[2,_,_,_]],S).
% sudoku4x4([[2,1,_,4],[_,3,_,_],[_,_,_,_],[_,_,_,2]],S).

%% show all 4x4 sudokus
% sudoku4x4([[_,_,_,_],[_,_,_,_],[_,_,_,_],[_,_,_,_]],S).
%% count the number of all 4x4 sudokus
% findall(0,sudoku4x4([[_,_,_,_],[_,_,_,_],[_,_,_,_],[_,_,_,_]],S),L),length(L,N).


%%% solves 6x6 sudokus
%% examples
% sudoku6x6([1,6,_,5,_,2, 5,_,3,_,1,4, _,1,2,_,6,_, 3,_,6,2,_,1, 6,_,_,_,2,_, 2,3,1,4,_,6], S).
% sudoku6x6([1,_,_,_,_,_, _,5,_,2,_,_, _,1,6,_,5,_, _,3,_,6,2,_, _,_,1,_,3,_, _,_,_,_,_,5], Solution).
% sudoku6x6([2,1,_,_,_,5, _,_,5,3,1,_, _,2,1,_,_,4, 3,_,_,1,2,_, _,4,_,6,_,_, 5,_,_,_,4,1], S).


%%% solves 9x9 sudokus
%% examples
% sudoku9x9([5,3,_,_,7,_,_,_,_, 6,_,_,1,9,5,_,_,_, _,9,8,_,_,_,_,6,_, 8,_,_,_,6,_,_,_,3, 4,_,_,8,_,3,_,_,1, 7,_,_,_,2,_,_,_,6, _,6,_,_,_,_,2,8,_, _,_,_,4,1,9,_,_,5, _,_,_,_,8,_,_,7,9], Solution).
% sudoku9x9([_,_,_,3,_,_,6,_,_, _,_,7,4,_,_,_,9,5, _,_,_,_,7,8,1,_,3, _,1,6,2,_,_,_,7,_, 3,_,8,_,_,_,_,_,_, _,_,_,_,_,_,9,2,_, 5,_,_,_,_,_,_,_,6, 2,_,_,_,_,3,_,_,_, _,_,_,1,_,9,_,_,_], Solution).
% sudoku9x9([_,_,_,_,_,_,_,_,_, _,_,_,_,_,3,_,8,5, _,_,1,_,2,_,_,_,_, _,_,_,5,_,7,_,_,_, _,_,4,_,_,_,1,_,_, _,9,_,_,_,_,_,_,_, 5,_,_,_,_,_,_,7,3, _,_,2,_,1,_,_,_,_, _,_,_,_,4,_,_,_,9], S).
% sudoku9x9([_,_,_,8,_,1,_,_,_, _,_,_,_,_,_,_,4,3, 5,_,_,_,_,_,_,_,_, _,_,_,_,7,_,8,_,_, _,_,_,_,_,_,1,_,_, _,2,_,_,3,_,_,_,_, 6,_,_,_,_,_,_,7,5, _,_,3,4,_,_,_,_,_, _,_,_,2,_,_,6,_,_], S).