#include <iostream>
#include <vector>
int n;
std::cin >> n;
int x, y, z;
x = 0;
y = 0;
z = 0;
for (int i = 0; i < n; i++)
{
    int newX, newY, newZ;
    std::cin >> newX >> newY >> newZ;
    x = x + newX;
    y = y + newY;
    z = z + newZ;
}
if (x == 0 && y == 0 && z == 0)
{
    count << "yes";
}
else
{
    cout << "no";
}
return 0;
