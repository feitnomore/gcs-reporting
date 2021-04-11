## Filename: cmd.py
 # Author: Marcelo Feitoza Parisi
 # 
 # Description: Responsible for
 # parsing cmd arguments.
 # 
 # ###########################
 # # DISCLAIMER - IMPORTANT! #
 # ###########################
 # 
 # Stuff found here was built as a
 # Proof-Of-Concept or Study material
 # and should not be considered
 # production ready!
 # 
 # USE WITH CARE!
##
import argparse

def args():
    # Main argument parser
    parser = argparse.ArgumentParser(prog="gcs-reporting", allow_abbrev=True, description='Cloud Storage bucket analysis tool', add_help=True, formatter_class=argparse.RawDescriptionHelpFormatter)

    # To parse subcommands
    subparsers = parser.add_subparsers(title='required command', dest='command', required=True)

    # Parse storageclass subcommand arguments
    arg_sc = subparsers.add_parser('storageclass', description='Cloud Storage bucket analysis tool: Storage Class Usage', help='consumption by storage class', add_help=True)
    req_arg_sc = arg_sc.add_argument_group('required options')
    req_arg_sc.add_argument('-b', '--bucket' , nargs=1, required=True, help='bucket to check usage')
    req_arg_sc.add_argument('-p', '--project', nargs=1, required=True, help='project id')

    # Parse size subcommand arguments (n = optional, default 10)
    arg_sz = subparsers.add_parser('size', description='Cloud Storage bucket analysis tool: Objects by Size', help='objects by size', add_help=True)
    req_arg_sz = arg_sz.add_argument_group('required options')
    req_arg_sz.add_argument('-b', '--bucket' , nargs=1,  required=True, help='bucket to check usage')
    req_arg_sz.add_argument('-p', '--project', nargs=1,  required=True, help='project id')
    arg_sz.add_argument('-r', '--reverse', action='store_false', required=False, help='reverse order')
    arg_sz.add_argument('-n', '--number' , type=int, required=False, default=10, help='number of entries to print [default: 10]')

    # Parse date subcommand arguments (n = optional, default 10)
    arg_dt = subparsers.add_parser('date', description='Cloud Storage bucket analysis tool: Objects by Date', help='objects by date', add_help=True)
    req_arg_dt = arg_dt.add_argument_group('required options')
    req_arg_dt.add_argument('-b', '--bucket' , nargs=1,  required=True, help='bucket to check usage')
    req_arg_dt.add_argument('-p', '--project', nargs=1,  required=True, help='project id')
    arg_dt.add_argument('-r', '--reverse', action='store_true', required=False, help='reverse order')
    arg_dt.add_argument('-n', '--number' , type=int, required=False, default=10, help='number of entries to print [default: 10]')

    # Parse date subcommand arguments (n = optional, default 10)
    arg_nm = subparsers.add_parser('name', description='Cloud Storage bucket analysis tool: Objects by Name', help='objects by name', add_help=True)
    req_arg_nm = arg_nm.add_argument_group('required options')
    req_arg_nm.add_argument('-b', '--bucket' , nargs=1,  required=True, help='bucket to check usage')
    req_arg_nm.add_argument('-p', '--project', nargs=1,  required=True, help='project id')
    arg_nm.add_argument('-r', '--reverse', action='store_true', required=False, help='reverse order')
    
    # Display each subcommand usage on -h / --help
    epilog = "commands usage:\n" "\t" + arg_sc.format_usage() + "\t" + arg_sz.format_usage() + "\t" + arg_dt.format_usage() + "\t" + arg_nm.format_usage() + ""
    parser.epilog = epilog

    args = parser.parse_args()

    return args
