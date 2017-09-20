#pragma once

#include <iostream>
#include <algorithm>
#include <time.h>
#include <conio.h>
#include <stdlib.h>

using namespace std;

enum Direction {LEFT, UP, RIGHT, DOWN};

class Game {
private:
	int field[4][4];
	int emptyX;
	int emptyY;

public:
	
	// initialize  
	void Init();	

	// run game
	void Run();

	// fill field
	void CreateField();
	
	// print field
	void DrawField();

	// move number
	void Move(Direction d);

	bool Win();
};