from pal.writer.comment.comment import CommentWriter
import textwrap


class YamlCommentWriter(CommentWriter):

    def declare_comment(self, outfile, comment, wrap):
        # Wrap at (wrap - 2) to account for "# "characters
        wrapped = textwrap.wrap(comment, width=(wrap - 2))
        for line in wrapped:
            outfile.write("# " + str(line))
            self.write_newline(outfile)
