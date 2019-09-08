import subprocess
import fire


'''
# get list of images in tab delimited format
aws ec2 describe-images --owners amazon --query "Images[*].[CreationDate, Name, Description]" --output text > tmp.txt

aws ec2 describe-images --owners amazon | jq -r '.Images[]|[.CreationDate, .ImageId, .Name, .Description]|@tsv'

# get dimensions of csv file (tab delimited with no header)
csvtk -t -H dim tmp.txt
'''

def run_pipe_cmds(*args):
    cmd = '|'.join(args)
    subprocess.run(cmd, shell=True)


class ListCommands:
    ' list aws resources '
    def deep_learning_ubuntu(self):
        ' images owned by amazon '
        aws_cmd = 'aws ec2 describe-images --owners amazon --filters Name="name",Values="Deep Learning AMI (Ubuntu)*"'
        jq_cmd = "jq -r '.Images[]|[.CreationDate, .ImageId, .Name, .Description]|@tsv'"
        sort_cmd = "sort"
        run_pipe_cmds(aws_cmd, jq_cmd, sort_cmd)

    def key_pairs(self):
        ' key pairs owned by current user '
        aws_cmd = "aws ec2 describe-key-pairs"
        jq_cmd = "jq -r '.KeyPairs[] | [.KeyName, .KeyFingerprint] | @tsv'"
        run_pipe_cmds(aws_cmd, jq_cmd)


class DescribeCommands:
    ' describe aws resources '
    def image(self, image_id):
        aws_cmd = f'aws ec2 describe-images --image-ids {image_id}'
        jq_cmd = "jq -C"
        run_pipe_cmds(aws_cmd, jq_cmd)


class Commands:
    ''' execute AWS cli commands '''

    def __init__(self):
        self.list = ListCommands()
        self.describe = DescribeCommands()


class IngestionStage(object):

    def run(self):
        return 'Ingesting! Nom nom nom...'


class DigestionStage(object):

    def run(self, volume=1):
        return ' '.join(['Burp!'] * volume)

    def status(self):
        return 'Satiated.'


class Pipeline(object):

    def __init__(self):
        self.ingestion = IngestionStage()
        self.digestion = DigestionStage()

    def run(self):
        print('in pipeline run')
        self.ingestion.run()
        self.digestion.run()


if __name__ == '__main__':
    fire.Fire(Commands)
    # fire.Fire(Pipeline)
