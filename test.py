import unittest
import tictactoe as ttt


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.EMPTY = None
        self.X = 'X'
        self.O = 'O'

    def test_initial_state(self):
        empty_board = \
            [[self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY]]
        self.assertEqual(empty_board, ttt.initial_state())


    def test_player_no_moves(self):
        player_board = \
            [[self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY]]

        self.assertEqual(self.X, ttt.player(player_board))


    def test_player_O_to_go(self):
        player_board = \
            [[self.X, self.O, self.X],
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY]]
        self.assertEqual(self.O, ttt.player(player_board))


    def test_player_X_to_go(self):
        player_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.EMPTY],
            [self.X, self.EMPTY, self.EMPTY]]
        self.assertEqual(self.X, ttt.player(player_board))


    def test_actions_empty_board(self):
        player_board = \
            [[self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY]]
        avail_moves = set((
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)))
        
        self.assertEqual(avail_moves, ttt.actions(player_board))


    def test_actions_game_in_progress(self):
        player_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.EMPTY],
            [self.X, self.EMPTY, self.EMPTY]]
        avail_moves = set((
            (1, 2),
            (2, 1), (2, 2)))
        
        self.assertEqual(avail_moves, ttt.actions(player_board))


    def test_actions_no_moves_left(self):
        player_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.X],
            [self.X, self.X, self.O]]
        avail_moves = None
        
        self.assertIsNone(avail_moves, ttt.actions(player_board))


    def test_result_valid_action(self):
        player_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.EMPTY],
            [self.X, self.EMPTY, self.EMPTY]]
        player_move = (1, 2)
        resulting_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.X],
            [self.X, self.EMPTY, self.EMPTY]]
        
        self.assertEqual(resulting_board, ttt.result(player_board, player_move))


    def test_result_invalid_action(self):
        player_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.EMPTY],
            [self.X, self.EMPTY, self.EMPTY]]
        player_move = (1, 1)
        resulting_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.X],
            [self.X, self.EMPTY, self.EMPTY]]

        self.assertRaises(ttt.ResultError)


    def test_winner(self):
        player_board = \
            [[self.X, self.O, self.O],
            [self.O, self.O, self.X],
            [self.X, self.X, self.X]]
        self.assertEqual(self.X, ttt.winner(player_board))

        player_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.X],
            [self.X, self.O, self.X]]
        self.assertEqual(self.O, ttt.winner(player_board))

        player_board = \
            [[self.X, self.O, self.X],
            [self.X, self.X, self.O],
            [self.O, self.O, self.X]]
        self.assertEqual(self.X, ttt.winner(player_board))

        player_board = \
            [[self.O, self.X, self.X],
            [self.O, self.X, self.O],
            [self.X, self.O, self.X]]
        self.assertEqual(self.X, ttt.winner(player_board))

        player_board = \
            [[self.X, self.X, self.X],
            [self.EMPTY, self.EMPTY, self.O],
            [self.O, self.EMPTY, self.EMPTY]]
        self.assertEqual(self.X, ttt.winner(player_board))


    def test_no_winner(self):
        player_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.EMPTY],
            [self.X, self.EMPTY, self.EMPTY]]
        self.assertIsNone(ttt.winner(player_board))

        player_board = \
            [[self.O, self.X, self.X],
            [self.X, self.O, self.O],
            [self.X, self.O, self.X]]
        self.assertIsNone(ttt.winner(player_board))


    def test_is_terminal(self):
        player_board = \
            [[self.O, self.X, self.X],
            [self.O, self.X, self.O],
            [self.X, self.O, self.X]]
        self.assertTrue(ttt.terminal(player_board))

        player_board = \
            [[self.O, self.X, self.X],
            [self.X, self.O, self.O],
            [self.X, self.O, self.X]]
        self.assertTrue(ttt.terminal(player_board))

        player_board = \
            [[self.O, self.EMPTY, self.X],
            [self.O, self.X, self.EMPTY],
            [self.X, self.O, self.X]]
        self.assertTrue(ttt.terminal(player_board))

    def test_is_not_terminal(self):
        player_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.EMPTY],
            [self.X, self.EMPTY, self.EMPTY]]
        self.assertFalse(ttt.terminal(player_board))


    def test_utility(self):
        # X wins
        player_board = \
            [[self.X, self.O, self.O],
            [self.O, self.O, self.X],
            [self.X, self.X, self.X]]
        self.assertEqual(1, ttt.utility(player_board))

        # O wins
        player_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.X],
            [self.X, self.O, self.X]]
        self.assertEqual(-1, ttt.utility(player_board))

        # tie
        player_board = \
            [[self.O, self.X, self.X],
            [self.X, self.O, self.O],
            [self.X, self.O, self.X]]
        self.assertEqual(0, ttt.utility(player_board))

        player_board = \
            [[self.X, self.O, self.X],
            [self.O, self.O, self.EMPTY],
            [self.X, self.EMPTY, self.EMPTY]]
        self.assertEqual(0, ttt.utility(player_board))


    def test_minimax_board_terminal(self):
        player_board = \
            [[self.O, self.X, self.X],
            [self.O, self.X, self.O],
            [self.X, self.O, self.X]]
        self.assertIsNone(ttt.minimax(player_board))


    @unittest.skip('wip')
    def test_minimax_board(self):

        #player_board = \
        #    [[self.EMPTY, self.X, self.O],
        #    [self.O, self.X, self.X],
        #    [self.X, self.EMPTY, self.O]]
        #optimal_move = (2, 1)
        #self.assertEqual(optimal_move, ttt.minimax(player_board))

        #player_board = \
        #    [[self.O, self.X, self.X],
        #    [self.X, self.O, self.EMPTY],
        #    [self.X, self.O, self.EMPTY]]
        #optimal_move = (2, 2)
        #self.assertEqual(optimal_move, ttt.minimax(player_board))

        #player_board = \
        #    [[self.O, self.X, self.X],
        #    [self.X, self.EMPTY, self.EMPTY],
        #    [self.X, self.O, self.O]]
        #optimal_move = (1, 1)
        #self.assertEqual(optimal_move, ttt.minimax(player_board))

        player_board = \
            [[self.X, self.O, self.O],
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.X]]
        optimal_move = (1, 1)
        self.assertEqual(optimal_move, ttt.minimax(player_board))
