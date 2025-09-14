/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: fchaput <fchaput@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/13 14:16:36 by fchaput           #+#    #+#             */
/*   Updated: 2025/09/14 12:59:20 by fchaput          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		ft_putchar(str[i]);
		i++;
	}
}

void ft_putnbr(int nb)
{
    if (nb < 0)
    {
        ft_putchar('-');
        nb = nb * -1;
    }
    if (nb >= 10)
    {
        ft_putnbr(nb / 10);
        ft_putchar(nb % 10 + '0');
    }
    if (nb < 10)
    {
        ft_putchar(nb + '0');
    }        
}

void	print_board(int board[3][3])
{
	int col;
	int row;
	
	col = 0;
	while (col < 4)
	{
		row = 0;
		while (row < 4)
		{
			ft_putnbr(board[col][row]);
			if (row < 3)
				ft_putchar(' ');
			row++;
		}
		ft_putchar('\n');
		col++;
	}
	row = 0;
}

/*int solve(int row, int col, int board[4][4], int clues[16])
{
	int n;

	if (row == 4)
	{
		check_views();
	}
	
}*/

int count_visible_right(int row, int col, int board[4][4])
{
	int i;
	int count_visible;
	int max;
	
	max = 0;
	i = 0;
	count_visible = 0;
	while (i <= 3)
	{
		if (board[col][row] > max)
		{
			max = board[col][row];
			i++;
			count_visible++;
		}
		i++;
	}
	
	return ()
	
}
int main()
{
	int board[3][3];
	int clues[16] =  {4, 3, 2, 1, 1, 2, 2, 2, 4, 3, 2, 1, 1, 2, 2, 2};
	
	print_board(board);
	return (0);
}

#include <stdio.h>

#define SIZE 4

int count_visible(int *line, int size)
{
    int visible = 0;
    int max_height = 0;
    int i = 0;

    while (i < size)
    {
        if (line[i] > max_height)
        {
            max_height = line[i];
            visible++;
        }
        i++;
    }
    return visible;
}

int check_grid(int grid[SIZE][SIZE], int *clues)
{
    int line[SIZE];
    int i = 0;
    int j;

    // Colonnes TOP
    while (i < SIZE)
    {
        j = 0;
        while (j < SIZE)
        {
            line[j] = grid[j][i];
            j++;
        }
        if (count_visible(line, SIZE) != clues[i])
            return 0;
        i++;
    }

    // Colonnes BOTTOM
    i = 0;
    while (i < SIZE)
    {
        j = 0;
        while (j < SIZE)
        {
            line[j] = grid[SIZE - 1 - j][i];
            j++;
        }
        if (count_visible(line, SIZE) != clues[SIZE + i])
            return 0;
        i++;
    }

    // Lignes LEFT
    i = 0;
    while (i < SIZE)
    {
        j = 0;
        while (j < SIZE)
        {
            line[j] = grid[i][j];
            j++;
        }
        if (count_visible(line, SIZE) != clues[2 * SIZE + i])
            return 0;
        i++;
    }

    // Lignes RIGHT
    i = 0;
    while (i < SIZE)
    {
        j = 0;
        while (j < SIZE)
        {
            line[j] = grid[i][SIZE - 1 - j];
            j++;
        }
        if (count_visible(line, SIZE) != clues[3 * SIZE + i])
            return 0;
        i++;
    }

    return 1;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./a.out \"clues\"\n");
        return 1;
    }

    int grid[SIZE][SIZE] = {
        {4, 3, 2, 1},
        {1, 2, 3, 4},
        {2, 1, 4, 3},
        {3, 4, 1, 2}
    };

    int clues[SIZE * 4];
    char *str = argv[1];
    int k = 0;
    int idx = 0;

    while (k < SIZE * 4)
    {
        clues[k] = str[idx] - '0';
        idx += 2; // on saute l'espace
        k++;
    }

    if (check_grid(grid, clues))
        printf("✅ Grille valide\n");
    else
        printf("❌ Grille invalide\n");

    return 0;
}
