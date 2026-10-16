% Facts
parking_slot(s1, car, available).
parking_slot(s2, bike, occupied).
parking_slot(s3, car, available).
parking_slot(s4, bike, available).
parking_slot(s5, car, occupied).

% Rule
available_slot(Type, Slot) :-
    parking_slot(Slot, Type, available).

% Query
% ?- available_slot(car, Slot).
