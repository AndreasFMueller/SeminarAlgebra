//
// 3dimage.pov -- -template for 3d images rendered by Povray
//
// (c) 2023 Prof Dr Andreas Müller
//
#include "../../../common/common.inc"
#include "farbdreiecke.inc"

#declare gitterfarbe = rgb<0.6,0.6,0.6>;
#declare gitterradius = 0.005;

place_camera(<33, 20, 50>, <0, 0.655, 0>, 16/9, 0.040)
lightsource(<10, 15, 40>, 1, White)

arrow(-2.20 * e1, 2.20 * e1, 0.01, White)
arrow(-0.30 * e2, 1.95 * e2, 0.01, White)
arrow(-1.20 * e3, 1.20 * e3, 0.01, White)

union {
	triangle { < -2, 0, -1>, <2, 0, -1>, <2, 0, 1> }
	triangle { < -2, 0, -1>, <2, 0, 1>, <-2, 0, 1> }
	#declare xmin = -2;
	#declare xmax = 2;
	#declare ymin = -1;
	#declare ymax = 1;
	#declare xstep = 0.2;
	#declare X = xmin;
	#while (X < xmax + xstep/2)
		cylinder { <X, 0, ymin>, <X, 0, ymax>, gitterradius }
		#declare X = X + xstep;
	#end
	#declare ystep = 0.2;
	#declare Y = ymin;
	#while (Y < ymax + ystep/2)
		cylinder { <xmin, 0, Y>, <xmax, 0, Y>, gitterradius }
		#declare Y = Y + ystep;
	#end
	sphere { < xmin, 0, ymin >, gitterradius }
	sphere { < xmax, 0, ymin >, gitterradius }
	sphere { < xmin, 0, ymax >, gitterradius }
	sphere { < xmax, 0, ymax >, gitterradius }
	pigment {
		color Gray
	}
	finish {
		metallic
		specular 0.99
	}
}

intersection {
	box { <-2.1,0, -1.1>, <2.1, 1.85, 1.1> }
	union {
		flaeche()
	}
}

intersection {
	box { <-2.1,0, -1.1>, <2.1, 1.85, 1.1> }
	union {
		gitter()
	}
	pigment {
		color gitterfarbe
	}
}

//box { <-2,0, -1>, <2, 1.85, 1>
//	pigment {
//		color White
//	}
//}
