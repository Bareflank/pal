from pal.writer.comment.comment import CommentWriter

import textwrap


class CMultilineCommentWriter(CommentWriter):

    def declare_comment(self, outfile, comment, wrap):
        # Wrap at (wrap - 3) to account for " * "characters
        wrapped = textwrap.wrap(comment, width=(wrap - 3))
        outfile.write("/*")
        self.write_newline(outfile)
        for line in wrapped:
            outfile.write(" * " + str(line))
            self.write_newline(outfile)
        outfile.write("*/")
        self.write_newline(outfile)

    def declare_file_documentation(self, outfile, summary, wrap, details=""):
        pass

    def declare_item_documentation(self, outfile, summary, wrap, details=""):
        pass
