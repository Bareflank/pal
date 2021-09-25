from pal.writer.comment.comment import CommentWriter


class NoneCommentWriter(CommentWriter):

    def declare_comment(self, outfile, comment, wrap):
        pass

    def declare_file_documentation(self, outfile, summary, wrap, details=""):
        pass

    def declare_item_documentation(self, outfile, summary, wrap, details=""):
        pass
