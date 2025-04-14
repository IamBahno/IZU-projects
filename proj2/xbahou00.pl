% Zadani c. 6:
% Napiste program resici ukol dany predikatem u6(LIN,VOUT), kde LIN je vstupni 
% ciselny seznam a VOUT je vystupni promenna, ve ktere se vraci hodnota -1/1/0, 
% pokud seznam LIN obsahuje pouze zaporna cisla/pouze kladna cisla/v ostatnich 
% pripadech (nula neni ani kladne, ani zaporne cislo). 

% Testovaci predikaty:                                   	% VOUT 
u6_1:- u6([5,27,-1,0, 16,-4],VOUT),write(VOUT).	        	% 0
u6_2:- u6([-5.3,-27,-1,-15.8,-5],VOUT),write(VOUT).	       	% -1
u6_3:- u6([6.1,28,2,1,16,4.2],VOUT),write(VOUT).       		% 1
u6_r:- write('Zadej LIN: '),read(LIN),u6(LIN,VOUT),write(VOUT).

%  Reseni:

u6(LIN,VOUT):-
    biggest_element(LIN,Max),
    smallest_element(LIN,Min),
    VOUT is Max - Min.

biggest_element([X], X).

biggest_element([X|Xs], Max) :- 
    biggest_element(Xs, MaxRest),
    MaxRest =< X,
    Max is X.

biggest_element([X|Xs], Max) :- 
    biggest_element(Xs, MaxRest),
    MaxRest > X,
    Max is MaxRest.

smallest_element([X], X).

smallest_element([X|Xs], Min) :- 
    biggest_element(Xs, MinRest),
    MinRest >= X,
    Min is X.

smallest_element([X|Xs], Min) :- 
    smallest_element(Xs, MinRest),
    MinRest < X,
    Min is MinRest.


%u6(LIN,VOUT):-
%    greater_than_0(LIN,VOUT).
%
%u6(LIN,VOUT):-
%    smaller_than_0(LIN,VOUT).
%
%u6(_,VOUT):-
%    VOUT is 0.
%
%
%greater_than_zero(X) :-
%    X > 0.
%
%is_zero([HEAD|_]) :-
%    HEAD =:= 0.
%
%greater_than_0([],VOUT):-
%    VOUT is 1.
%
%greater_than_0([HEAD|TAIL],VOUT):-
%    HEAD > 0,
%    greater_than_0(TAIL,VOUT),
%    VOUT is 1. 
%
%smaller_than_0([],VOUT):-
%    VOUT is -1.
%
%smaller_than_0([HEAD|TAIL],VOUT):-
%    HEAD < 0,
%    smaller_than_0(TAIL,VOUT),
%    VOUT is -1. 


