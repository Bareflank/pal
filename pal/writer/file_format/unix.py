from pal.writer.file_format.file_format import FileFormatWriter


class UnixFileFormatWriter(FileFormatWriter):

    def write_newline(self, outfile, count=1):
        for i in range(count):
            outfile.write("\n")

    def write_indent(self, outfile, count=1):
        for i in range(count):
            outfile.write("    ")
