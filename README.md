# Tic Tac Toe AI 🎮

A Tic Tac Toe game implementation with AI opponents using **Minimax** and **Alpha-Beta Pruning** algorithms. This project was developed for an Artificial Intelligence course to demonstrate and compare game tree search algorithms.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Features

- **Two AI Algorithms**:
  - **Minimax**: Classic game tree search algorithm
  - **Alpha-Beta Pruning**: Optimized version with branch pruning  
  
- **Beautiful Pygame GUI**:
  - Modern and intuitive interface
  - Smooth animations
  - Responsive controls  
  
- **Performance Metrics**:
  - Real-time display of nodes visited
  - Execution time measurement
  - Algorithm comparison

- **Interactive Gameplay**:
  - Choose your AI opponent
  - Visual feedback
  - Play again functionality

## 📋 Requirements

- Python 3.7 or higher
- Pygame 2.0 or higher

## 🚀 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/alibakhsha/tic_tac_toe_ai.git
cd tic_tac_toe_ai
```

2. **Install dependencies**:
```bash
pip install pygame
```

## 🎮 How to Run

```bash
python main_pygame.py
```

## 🕹️ How to Play

1. **Start Screen**: Choose your AI opponent
   - Click "Minimax Algorithm" for classic Minimax
   - Click "Alpha-Beta Pruning" for optimized version

2. **Game Screen**: 
   - You play as **X** (cross)
   - AI plays as **O** (circle)
   - Click on any empty cell to make your move
   - AI will automatically respond

3. **Game Stats**: 
   - Algorithm name is displayed at the bottom
   - After each AI move, you'll see:
     - Number of nodes visited
     - Execution time in seconds

4. **End Game**:
   - Winner is announced with color-coded message
   - Click "Play Again" to restart

## 📁 Project Structure

```
tic_tac_toe_ai/
│
├── game.py              # Core game logic and board management
├── minimax.py           # Minimax algorithm implementation
├── alphabeta.py         # Alpha-Beta pruning implementation
├── main_pygame.py       # Pygame GUI
│
└── README.md           # Documentation
```

## 🧠 Algorithm Overview

### Minimax Algorithm
The Minimax algorithm explores the entire game tree to find the optimal move. It assumes both players play optimally.

- **Pros**: Guaranteed optimal solution
- **Cons**: Explores all possible states (slower)

### Alpha-Beta Pruning
An optimization of Minimax that eliminates branches that don't need to be explored.

- **Pros**: Significantly faster, same optimal result
- **Cons**: Slightly more complex implementation

### Performance Comparison

| Algorithm | Avg Nodes Visited | Avg Time |
|-----------|-------------------|----------|
| Minimax   | ~5,000-50,000     | 0.01-0.5s |
| Alpha-Beta| ~500-5,000        | 0.001-0.05s |

*Note: Actual performance varies based on game state*

## 🎨 Game Components

### game.py
- `TicTacToe` class: Manages game state
- `available_moves()`: Returns list of valid moves
- `make_move()`: Places a mark on the board
- `is_winner()`: Checks for winning condition
- `is_draw()`: Checks for draw condition
- `evaluate()`: Returns game state value

### minimax.py
- `minimax()`: Recursive Minimax implementation
- Tracks nodes visited for performance analysis

### alphabeta.py
- `alphabeta()`: Alpha-Beta pruning implementation
- Optimized tree traversal with pruning

### main_pygame.py
- Complete Pygame GUI implementation
- Start screen with algorithm selection
- Game screen with visual board
- End screen with results
- Performance stats display

## 🎓 Educational Purpose

This project demonstrates:
- Game tree search algorithms
- Adversarial search in AI
- Performance optimization techniques
- Algorithm comparison and analysis
- Clean code practices in Python

## 📊 Understanding the Stats

When you play, you'll see metrics like:
```
AI Move: 2847 nodes visited in 0.0234s
```

This means:
- **Nodes visited**: Number of game states evaluated
- **Time**: How long the AI took to decide
- Lower numbers indicate better pruning efficiency

## 🎯 Tips for Playing

- The AI is **unbeatable** when playing optimally
- Best you can do is **draw** against the AI
- Try both algorithms to see the performance difference
- Alpha-Beta will make the same moves as Minimax, but faster

## 🛠️ Customization

### Adjust Colors
In `main_pygame.py`, customize:
```python
BG_COLOR = (28, 170, 156)      # Background
LINE_COLOR = (23, 145, 135)     # Grid lines
CIRCLE_COLOR = (239, 231, 200)  # O symbol
CROSS_COLOR = (66, 66, 66)      # X symbol
```

### Modify Board Size
In `main_pygame.py`:
```python
WIDTH, HEIGHT = 600, 700
SQUARE_SIZE = 200
```

## 🐛 Troubleshooting

### Pygame not found
```bash
pip install --upgrade pygame
```

### Import errors
Make sure all files are in the same directory:
- game.py
- minimax.py
- alphabeta.py
- main_pygame.py

### Slow performance
- This is normal for Minimax with early-game states
- Try Alpha-Beta for better performance
- Check console output for detailed timing

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Ali Bakhsha**
- GitHub: [@alibakhsha](https://github.com/alibakhsha)

## 🙏 Acknowledgments

- Developed for Artificial Intelligence course
- Inspired by classic AI game theory
- Built with Python and Pygame

## 📚 Further Reading

- [Minimax Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Minimax)
- [Alpha-Beta Pruning - Wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
- [Game Theory in AI](https://en.wikipedia.org/wiki/Game_theory)

---

**Enjoy playing against the AI! 🤖**