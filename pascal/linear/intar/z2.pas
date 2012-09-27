program z2;
	uses crt;
var
	day,wday: Integer;

begin
	writeln('Enter the day of year');
	read(day);
	writeln('Enter the first week day of year');
	read(wday);
	day := (day+wday-2) mod 7 + 1;
	writeln('The day of week is ', day);
readkey;
end.
