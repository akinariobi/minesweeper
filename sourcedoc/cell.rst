==================
:mod:`cell` module
==================


Ce module définit une classe pour représenter les cellules (ou cases) d'un plateau de
jeu de démineur.

Une cellule peut être

* cachée ou révélée (ou encore découverte)
* elle peut ou non contenir une bombe
* son voisinage (les cellules voisines) contient un certain nombre de bombes
* elle peut avoir été jugée comme contenant hypothétiquement une bombe.



Class description
-----------------

.. autoclass:: cell.Cell

Methods
-------

.. automethod:: cell.Cell.is_revealed

.. automethod:: cell.Cell.reveal

.. automethod:: cell.Cell.is_bomb

.. automethod:: cell.Cell.set_bomb

.. automethod:: cell.Cell.is_hypothetic

.. automethod:: cell.Cell.set_hypothetic
								
.. automethod:: cell.Cell.unset_hypothetic

.. automethod:: cell.Cell.number_of_bombs_in_neighborhood
								
.. automethod:: cell.Cell.incr_number_of_bombs_in_neighborhood
	
			   
Special method
--------------

Only two special methods for this class.

.. automethod:: cell.Cell.__init__

.. automethod:: cell.Cell.__str__
								
