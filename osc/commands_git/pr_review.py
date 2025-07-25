import osc.commandline_git


# we decided not to use the command name 'pull' because that could be confused
# with the completely unrelated 'git pull' command


class PullRequestReviewCommand(osc.commandline_git.GitObsCommand):
    """
    Manage pull request reviews
    """

    name = "review"
    parent = "PullRequestCommand"

    def init_arguments(self):
        pass

    def run(self, args):
        self.parser.print_help()
