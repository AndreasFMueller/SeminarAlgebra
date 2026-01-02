%
% shadow.m -- find good initial conditions for newton iteration
%
% (c) 2026 Prof Dr Andreas Müller
%
format long
d = 0;
while (d == 0)
	d = 1;
	x0 = rand(1,1)
	x = x0;
	for i = (1:30)
		x = x - (x^2 + 1) / (2 * x);
		if (abs(x) < 0.1)
			d = 0;
		end
		if (abs(x) > 9.9)
			d = 0;
		end
	end
end

x = x0;
for i = (1:30)
	x = x - (x^2 + 1) / (2 * x)
end
