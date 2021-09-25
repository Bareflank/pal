from pal.writer.comment.comment import CommentWriter
import textwrap


class RustCommentWriter(CommentWriter):

    def declare_comment(self, outfile, comment, wrap):
        # Wrap at (wrap - 3) to account for "// "characters
        wrapped = textwrap.wrap(comment, width=(wrap - 3))
        for line in wrapped:
            outfile.write("// " + str(line))
            self.write_newline(outfile)

    def declare_file_documentation(self, outfile, summary, wrap, details=""):
        self._declare_documentation(outfile, "//!", summary, details, wrap)

    def declare_item_documentation(self, outfile, summary, wrap, details=""):
        self._declare_documentation(outfile, "///", summary, details, wrap)

    def _declare_documentation(self, outfile, prefix, summary, details, wrap):
        # Never wrap the summary
        summary = self._escape_docstring(str(summary))
        outfile.write(str(prefix) + " " + str(summary))
        self.write_newline(outfile)

        if str(details):
            outfile.write(str(prefix))
            self.write_newline(outfile)

            wrapped = textwrap.wrap(
                self._escape_docstring(str(details)),
                width=(wrap - len(str(prefix)))
            )

            for line in wrapped:
                outfile.write(prefix + " " + line)
                self.write_newline(outfile)

    def _escape_docstring(self, text):
        need_escaping = ['[', ']']

        for ch in need_escaping:
            text = text.replace(ch, "\\" + ch)

        return text
