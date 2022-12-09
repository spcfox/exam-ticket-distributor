import os
import sys
import argparse
from ticket_distributor import TicketDistributor


def main():
    args = parse_args()

    try:
        students = read_students(args.file)
    except FileNotFoundError:
        print(f'File {args.file} not found')
        sys.exit(1)
    except PermissionError:
        print(f'Permission denied for file {args.file}')
        sys.exit(1)
    except Exception as e:
        print(f'Unexpected read error: {e}')
        sys.exit(1)

    ticket_distributor = TicketDistributor(args.min_ticket, args.max_ticket, args.parameter)
    tickets = ticket_distributor.distribute(students)

    if args.output is None:
        write_tickets(sys.stdout, students, tickets, args.delimiter)
    else:
        try:
            out_dir = os.path.dirname(args.output)
            if out_dir:
                os.makedirs(os.path.dirname(args.output), exist_ok=True)

            with open(args.output, 'w') as file:
                try:
                    write_tickets(file, students, tickets, args.delimiter)
                except PermissionError:
                    print(f'Permission denied for file {args.output}')
                    sys.exit(1)
        except PermissionError:
            print(f'Permission denied for directory {os.path.dirname(args.output)}')
            sys.exit(1)
        except Exception as e:
            print(f'Unexpected write error: {e}')
            sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(prog='exam_ticket_distributor', description='Distribute tickets to students')
    parser.add_argument('file', type=str, help='Path to file with students')
    parser.add_argument('max_ticket', type=int, help='Max ticket number')
    parser.add_argument('-m', '--min_ticket', type=int, default=1, help='Min ticket number, default: 1')
    parser.add_argument('-p', '--parameter', type=str, default='',
                        help='Parameter for ticket distribution, default: empty')
    parser.add_argument('-o', '--output', type=str, default=None, help='Output file, default: stdout')
    parser.add_argument('-d', '--delimiter', type=str, default='.', help='Delimiter for name and ticket, default: .')

    return parser.parse_args()


def read_students(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return list(filter(bool, [line.strip() for line in file]))


def write_tickets(file, students: list[str], tickets: list[int], delimiter: str):
    assert len(students) == len(tickets)
    line_length = 3 + max([len(students[i]) + len(str(tickets[i])) for i in range(len(students))])
    for student, ticket in zip(students, tickets):
        delimiter_str = delimiter * (line_length - len(student) - len(str(ticket)) - 1)
        file.write(f'{student}{delimiter_str}{ticket}\n')


if __name__ == '__main__':
    main()
