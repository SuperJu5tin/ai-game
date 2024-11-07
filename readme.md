# AI Game
================

A simple text-based adventure game that pits you against enemies with varying difficulty levels.

## Table of Contents

* [Installation](#installation)
* [How to Play](#how-to-play)
* [Game Mechanics](#game-mechanics)
* [Classes and Stats](#classes-and-stats)
* [ enemy AI](#enemy-ai)

## Installation
-------------

To play the game, simply clone this repository and run `python game.py` in your terminal.

## How to Play
--------------

1. Choose a class for yourself (Warrior, Mage, or Rogue).
2. Select a set of stats for your character.
3. Engage in combat with an enemy with varying difficulty levels.

Use the following commands to interact with the game:

* `Attack` to deal damage to the enemy.
* `Use Magic` to cast a magical spell on the enemy.
* `Quit` to exit the game.

## Game Mechanics
--------------

The game is won when your health reaches zero. The enemy's health decreases based on the difficulty level and your chosen class.

### Classes and Stats

| Class | Description |
| --- | --- |
| Warrior | Strong melee attacker with high health. |
| Mage | Magical spellcaster with moderate health. |
| Rogue | Stealthy assassin with low health but high agility. |

**Stats**

* Strength (STR): Melee attack power.
* Agility (AGI): Movement speed and evasion chance.
* Magic (MGC): Spellcasting ability.

## Enemy AI
-------------

Enemies have a basic AI that makes them more difficult to defeat as their health decreases. They will:

* Attack you more frequently when their health is high.
* Use a random attack strategy when their health is low.

Note: This is a simplified implementation of an enemy AI and may not be suitable for more complex games.

## Contributing
------------

Pull requests are welcome! If you'd like to contribute to the game, please fork this repository and submit a pull request with your changes.