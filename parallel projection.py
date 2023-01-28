"""problem = 1781A Parallel projections
Vika's house has a room in a shape of a rectangular parallelepiped (also known as a rectangular cuboid). Its floor is a rectangle of size w×d, and the ceiling is right above at the constant height of h. Let's introduce a coordinate system on the floor so that its corners are at points (0,0), (w,0), (w,d), and (0,d).
A laptop is standing on the floor at point (a,b). A projector is hanging on the ceiling right above point (f,g).Vika wants to connect the laptop and the projector with a cable in such a way that the cable always goes along the walls, ceiling, or floor (i. e. does not go inside the cuboid). Additionally, the cable should always run parallel to one of the cuboid's edges (i. e. it can not go diagonally).
What is the minimum length of a cable that can connect the laptop to the projector?

Input
Each test contains multiple test cases. The first line contains the number of test cases t(1≤t≤104). The description of the test cases follows.
The first line of each test case contains three integers w, d, and h (2≤w,d,h≤1000) — the size of the room.
The second line contains four integers a, b, f, g (0<a,f<w ; 0<b,g<d): the laptop is located on the floor at point (a,b), while the projector is hanging on the ceiling right above point (f,g).

Output
For each test case, print a single integer — the minimum length of the cable connecting the laptop and the projector that runs only along the walls, floor, and ceiling parallel to cuboid's edges."""

#Solution
s=int(input())
while(s!=0):
    w,d,h=map(int,input().split())
    a,b,f,g=map(int,input().split())
    print(h+min((a+f+abs(b-g)),(w-a+w-f+abs(b-g)),(b+g+abs(a-f)),(d-b+d-g+abs(a-f))))
    s=s-1