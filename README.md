# Turing Machine & Binary Sum

# Contact information
- Gustavo Alfredo Zárate Acosta / gustavoza20@hotmail.com
- Fernando Nateras Bautista / fnaterasb1@gmail.com
- José Vidal Cardona Rosas / vrosas832@gmail.com

# Type of licence
GNU General Public License v3.0

# Resume 
* About the model of Turing Machine and adaptation for binary sum with Python3

# Software Tools
* Python3

# Description of Turing Machine
![TuringMachine](imagenes/TuringMachine.png)

 **Turing Machine**: Is building with:
  * A **tape** divided into cells where each cells contains a simbol from some finite alphabet. 
  >> The alphabet contains a special symbol called white (here written as 'B') it's like a symbol that tells us that there is no value.
  * A **head** that can read and write symbols on the tape and move the tape left and right one (and only one) cell at a time.
  * A **status record** that stores the status of the Turing machine, one of the finite states. There is a special initial state with which the status log starts.
  * A **finite table** of instructions (occasionally called an action table or transition function).
  
*for more information, see: [Turing Machine](https://es.wikipedia.org/wiki/M%C3%A1quina_de_Turing)*


> Our program is in the tape, and our head will move left or right
depending the instructions in the Card Number 1. The Card Number 1 contains the 
instructions for behavior of head. 
