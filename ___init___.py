"""
This module inserts the magic key and allows to turn it on or off.

Examples:
    >>> import magic_key
    >>> from .examples.person import Person

    >>> merlin = Person("Myrddin Wyllt", 42, "Caledonia") 
    >>> magic_key.turn_on(merlin, magic_type = None)
    >>> @`merlin.name()`
    Myrddin Wyllt

    >>> @merlin What is your first name?
    Invalid .. .  # TODO add actual error

    >>>
    >>> # Using the string matching engine
    >>> magic_key.turn_on(merlin, magic_type = True)
    >>> @merlin What is your first name?
    Myrddin Wyllt

    >>>
    >>> # Using the intellegence engine
    >>> magic_key.turn_on(merlin, magic_type = True)
    
    >>> @`merlin.name()`
    Myrddin Wyllt

    >>> @merlin Please, can you remind me, what is your first name?  It's M... ?
    Merlin, people also call me Merlinus and Myrddin. Please, feel free to call me Merlin. It is easier this way in English.

    >>> magic_key.turn_off(merlin)      # By default, this backs up the episode and consolidates the memory
"""

def turn_on(object, magic_type=None):
    """
    Activates the connector between the python interpreter and intellegence engine. Uses no magic by default.
    :param magic_type: Can be None, False or True. Specifies the type of magic to use in string matching.
    """

    match magic_type:
        case None:              # exact sting matching
            pass

        case False:              # whoosh engine sting matching
            pass

        case None:              # intellegence engine sting matching
            pass
