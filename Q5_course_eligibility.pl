% Facts
python_result(arun, pass).
python_result(bala, pass).
python_result(charan, pass).
python_result(divya, fail).

ds_result(arun, pass).
ds_result(bala, fail).
ds_result(charan, pass).
ds_result(divya, pass).

% Rule
eligible(X) :-
    python_result(X, pass),
    ds_result(X, pass).

% Query
% ?- eligible(X).
