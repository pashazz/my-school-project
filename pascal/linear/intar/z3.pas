program z3;
	uses crt;
var
	weekday,day,res: Integer;
begin
	clrscr;
	writeln('Enter first weekday of year, then <RET>, then day of year');
	read (weekday,day);
	res :=  (day mod 7) +  (7 - weekday) + (day div 7);
	writeln('The day of week is', res);

end.
