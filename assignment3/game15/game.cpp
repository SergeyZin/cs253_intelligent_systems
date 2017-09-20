#include "game.h"

void Game::Init() {
	CreateField();
	DrawField();
}

void Game::Run() {
	char ch;
	while (!Win()) {
		ch = _getch();

		switch (ch) {
		case 75: 
			Move(LEFT); 
			break;
		case 72: 
			Move(UP); 
			break; 
		case 77: 
			Move(RIGHT); 
			break; 
		case 80: 
			Move(DOWN); 
			break;
		case 27:
			return;
		}

		DrawField();
	}
	cout << "\n You win!";
}

void Game::CreateField() {
	bool numIsFree[15]; 
	int nums[15]; 
	
	for (int i = 0; i < 15; ++i)
		numIsFree[i] = true;
	
	bool ok;
	int randNum;
	srand(time(0));
	for (int i = 0; i < 15; ++i) {
		ok = false;
		while (!ok) {
			randNum = rand() % 15 + 1;
			if (numIsFree[randNum - 1])
				ok = true;
		}
		nums[i] = randNum;
		numIsFree[randNum - 1] = false;
	}
	
	int chaos = 0;
	int currNum = 0;

	for (int i = 0; i < 14; ++i) {
		currNum = nums[i];
		for (int j = i + 1; j < 15; ++j) {
			if (currNum > nums[j])
				++chaos;
		}
	}

	if (chaos % 2 == 1)
		swap(nums[13], nums[14]);

	for (int i = 0; i < 15; ++i) 
		field[i % 4][i / 4] = nums[i];

	field[3][3] = 0;
	emptyX = 3;
	emptyY = 3;
}

void Game::DrawField() {
	system("cls");
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
			if (field[j][i]) 
				printf("%3d", field[j][i]);
			else 
				printf("  _");
			printf("\n\n");
	}
	printf("\n\n");
}

void Game::Move(Direction d) {
	switch (d) {
	case LEFT:
		if (emptyX < 3) {
			field[emptyX][emptyY] = field[emptyX + 1][emptyY];
			field[emptyX + 1][emptyY] = 0;
			++emptyX;
		}
		break;
	case UP:
		if (emptyY < 3) {
			field[emptyX][emptyY] = field[emptyX][emptyY + 1];
			field[emptyX][emptyY + 1] = 0;
			++emptyY;
		}
		break;
	case RIGHT:
		if (emptyX > 0) {
			field[emptyX][emptyY] = field[emptyX - 1][emptyY];
			field[emptyX - 1][emptyY] = 0;
			--emptyX;
		}
		break;
	case DOWN:
		if (emptyY > 0) {
			field[emptyX][emptyY] = field[emptyX][emptyY - 1];
			field[emptyX][emptyY - 1] = 0;
			--emptyY;
		}
	}
}

bool Game::Win() {
	for (int i = 0; i < 15; ++i) {
		if (field[i % 4][i / 5] != i + 1)
			return false;
	}
	return true;
}

