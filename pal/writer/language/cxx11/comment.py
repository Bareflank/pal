import textwrap


class Cxx11CommentWriter():

    def declare_comment(self, outfile, comment, wrap=79):
        # Wrap at (wrap - 3) to account for " * "characters
        wrapped = textwrap.wrap(comment, width=(wrap - 3))
        outfile.write("/*")
        self.write_newline(outfile)
        for line in wrapped:
            outfile.write(" * " + str(line))
            self.write_newline(outfile)
        outfile.write("*/")
        self.write_newline(outfile)
