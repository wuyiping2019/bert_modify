import argparse
parser = argparse.ArgumentParser()
vocab_file = 'chinese_L-12_H-768_A-12/vocab.txt'
bert_config_file = 'chinese_L-12_H-768_A-12/bert_config.json'
bert_checkpoint = 'chinese_L-12_H-768_A-12/'
parser.add_argument("--input_file",
                    default=None,
                    type=str,
                    required=True,
                    help="")
parser.add_argument("--vocab_file",
                    default=None,
                    type=str,
                    required=True,
                    help="")
parser.add_argument("--bert_config_file",
                    default=None,
                    type=str,
                    required=True,
                    help="")
parser.add_argument("--init_checkpoint",
                    default=None,
                    type=str,
                    required=True,
                    help="")
parser.add_argument("--output_file",
                    default=None,
                    type=str,
                    required=True,
                    help="")
# flags.mark_flag_as_required("input_file")
#   flags.mark_flag_as_required("vocab_file")
#   flags.mark_flag_as_required("bert_config_file")
#   flags.mark_flag_as_required("init_checkpoint")
#   flags.mark_flag_as_required("output_file")