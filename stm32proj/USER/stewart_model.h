#include "math.h"
#include "light_matrix.h"

#define RAD2DEG 57.295779
#define DEG2RAD 0.017453
#define PI 3.1415926






// public:
// init func
void init_stewart_params(void);
// in: [x,y,z,roll,pitch,yaw] unit:mm & radian ; out:[leg1,leg2,leg3,leg4,leg4,leg6] unit:mm
void get_inv_solution(const float * in, float * out);

// private:
void get_rotation_matrix(Mat * mat, float rx, float ry, float rz) ;
float get_norm(Mat *src);
