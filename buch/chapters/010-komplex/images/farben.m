%
% farben.m
%
% (c) 2026 Prof Dr Andreas Müller
%
global N;
N = 100;

global h;
h = 1/N;

global saturation;
saturation = 0.9;

global value;
value = 1;

global offset;
offset = 1;

function retval = f(z)
	global offset;
	retval = 0.3 * (1/(z-offset) + 1/(z+offset));
end

function punkt(fn, p)
	fprintf(fn, "< %.4f, %.4f, %.4f >", p(1,1), p(1,3), p(1,2));
end

function retval = hue(w)
	phi0 = arg(f(w));
	retval = 360 * (phi0 + pi) / (2 * pi);
end

function quadrat(fn, z)
	global h;
	global saturation;
	global value;
	global offset;
	fprintf(fn, "// z = %.3f + %.3fi\n", real(z), imag(z));
	z00 = z;
	if (z00 == offset) || (z00 == -offset)
		return;
	end
	z10 = z +           h;
	if (z10 == offset) || (z10 == -offset)
		return;
	end
	z01 = z +      i  * h;
	if (z01 == offset) || (z01 == -offset)
		return;
	end
	z11 = z + (1 + i) * h;
	if (z11 == offset) || (z11 == -offset)
		return;
	end
	p00 = [ real(z00), imag(z00), abs(f(z00)) ];
	p10 = [ real(z10), imag(z10), abs(f(z10)) ];
	p01 = [ real(z01), imag(z01), abs(f(z01)) ];
	p11 = [ real(z11), imag(z11), abs(f(z11)) ];
	phi0 = arg(f(z +     (1+i) * h/3));
	phi1 = arg(f(z + 2 * (1+i) * h/3));
	fprintf(fn, "triangle {\n\t");
	punkt(fn, p00);
	fprintf(fn, ",\n\t");
	punkt(fn, p10);
	fprintf(fn, ",\n\t");
	punkt(fn, p01);
	fprintf(fn, "\n\tpigment {\n\t\t color CHSV2RGB(rgb<%.3f, %.2f, %.2f>)\n\t}",
		hue(z + (1+i)*h), saturation, value);
	fprintf(fn, "\n\tfinish {\n\t\tmetallic\n\t\tspecular 0.99\n");
	fprintf(fn, "\t}\n}\n");
	fprintf(fn, "triangle {\n\t");
	punkt(fn, p10);
	fprintf(fn, ",\n\t");
	punkt(fn, p11);
	fprintf(fn, ",\n\t");
	punkt(fn, p01);
	fprintf(fn, "\n\tpigment {\n\t\t color CHSV2RGB(rgb<%.3f, %.2f, %.2f>)\n\t}",
		hue(z + 2*(1+i)*h), saturation, value);
	fprintf(fn, "\n\tfinish {\n\t\tmetallic\n\t\tspecular 0.99\n");
	fprintf(fn, "\t}\n}\n");
end

global xmin;
xmin = -2;
global xmax;
xmax = 2;
global ymin;
ymin = -1;
global ymax;
ymax = 1;

function	xgitterlinie(fn, x)
	global ymin;
	global ymax;
	global h;
	global N;
	global offset;
	for iy = (0:(2*N-1))
		z0 = x + i * (ymin + iy * h);
		if (z0 == offset) || (z0 == -offset)
			return;
		end
		p0 = [ real(z0), imag(z0), abs(f(z0)) ];
		z1 = z0 + i * h;
		if (z1 == offset) || (z1 == -offset)
			return;
		end
		p1 = [ real(z1), imag(z1), abs(f(z1)) ];
		fprintf(fn, "sphere { ");
		punkt(fn, p0);
		fprintf(fn, ", gitterradius }\n");
		fprintf(fn, "cylinder { ");
		punkt(fn, p0);
		fprintf(fn, ", ");
		punkt(fn, p1);
		fprintf(fn, ", gitterradius }\n");
	end
	z0 = x + ymax * i;
	p0 = [ real(z0), imag(z0), abs(f(z0)) ];
	fprintf(fn, "sphere { ");
	punkt(fn, p0);
	fprintf(fn, ", gitterradius }\n");
end

function	ygitterlinie(fn, y)
	global xmin;
	global xmax;
	global h;
	global N;
	global offset;
	for ix = (0:(4*N-1))
		z0 = xmin + ix * h + y * i;
		if (z0 == offset) || (z0 == -offset)
			return;
		end
		p0 = [ real(z0), imag(z0), abs(f(z0)) ];
		z0 = xmin + ix * h + y * i;
		z1 = z0 + h;
		if (z1 == offset) || (z1 == -offset)
			return;
		end
		p1 = [ real(z1), imag(z1), abs(f(z1)) ];
		fprintf(fn, "sphere { ");
		punkt(fn, p0);
		fprintf(fn, ", gitterradius }\n");
		fprintf(fn, "cylinder { ");
		punkt(fn, p0);
		fprintf(fn, ", ");
		punkt(fn, p1);
		fprintf(fn, ", gitterradius }\n");
	end
	z0 = xmax + y * i;
	p0 = [ real(z0), imag(z0), abs(f(z0)) ];
	fprintf(fn, "sphere { ");
	punkt(fn, p0);
	fprintf(fn, ", gitterradius }\n");
end

fn = fopen("farbdreiecke.inc", "w");

fprintf(fn, "#macro flaeche()\n");

for ix = (0:(4*N-1))
	x = xmin + ix * h;
	for iy = (0:(2*N-1))
		y = ymin + iy * h;
		z = x + i*y;
		quadrat(fn, z);
	end
end

fprintf(fn, "#end\n");

fprintf(fn, "#macro gitter()\n");

for x = (xmin:0.2:xmax)
	xgitterlinie(fn, x);
end
for y = (ymin:0.2:ymax)
	ygitterlinie(fn, y);
end

fprintf(fn, "#end\n");

fclose(fn);

