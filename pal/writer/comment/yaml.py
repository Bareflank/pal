from pal.writer.comment.comment import CommentWriter
import textwrap


class YamlCommentWriter(CommentWriter):

    def declare_comment(self, outfile, comment, wrap):
        # Wrap at (wrap - 2) to account for "# "characters
        wrapped = textwrap.wrap(comment, width=(wrap - 2))
        for line in wrapped:
            outfile.write("# " + str(line))
            self.write_newline(outfile)

    def declare_file_documentation(self, outfile, summary, wrap, details=""):
        pass

    def declare_item_documentation(self, outfile, summary, wrap, details=""):
        pass
