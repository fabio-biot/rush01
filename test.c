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
