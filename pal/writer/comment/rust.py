from pal.writer.comment.comment import CommentWriter
import textwrap


class RustCommentWriter(CommentWriter):

    def declare_comment(self, outfile, comment, wrap):
        # Wrap at (wrap - 3) to account for "// "characters
        wrapped = textwrap.wrap(comment, width=(wrap - 3))
        for line in wrapped:
            outfile.write("// " + str(line))
            self.write_newline(outfile)
