# Exam Ticket Distributor

Exam Ticket Distributor is a script that allows you to distribute exam tickets to students in a class.
Ticket distribution implemented using a cryptographic hash function keccak256.
Therefore, distribution is uniform and depends on the student's name but not on the students order in the list.
If you need to get a different distribution for the same students, you can specify a parameter.

## Run

To run the script, you need to have installed Python 3.6 or higher.
Then you need to install the dependencies from the requirements.txt file.
To do this, run the command:
```bash
    pip install -r requirements.txt
```

After that, you can run the script:
```bash
    python exam_ticket_distributor.py file max_ticket_number
```

## Parameters

The script takes the following parameters:

```
positional arguments:
  file                  Path to file with students
  max_ticket            Max ticket number

options:
  -h, --help            show this help message and exit
  -m MIN_TICKET, --min_ticket MIN_TICKET
                        Min ticket number, default: 1
  -p PARAMETER, --parameter PARAMETER
                        Parameter for ticket distribution, default: empty
  -o OUTPUT, --output OUTPUT
                        Output file, default: stdout
  -d DELIMITER, --delimiter DELIMITER
                        Delimiter for name and ticket, default: .
```

## Example

```bash
    python exam_ticket_distributor.py example/students_example.txt 10 -o example/tickets_example.txt
```

You can sae an example of the output file in the [example/tickets_example.txt](example/tickets_example.txt) file.