# Section 7: Files and File Systems — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). The console demos use `ls`, `xxd`, and `file`.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | Files, File Systems, and Paths | 1.1–1.5 | about 4 min |
| 2 | Metadata, Magic Bytes, and Deletion | 2.1–2.5 | about 4 min |

---

## Video 1 — Files, File Systems, and Paths

### 1.1 — Title

**Show:** slide 1.1

**Say:** Last lesson we looked at a running program in memory. This lesson is about data at rest, on disk, when nothing is running: files. We'll see what a file really is, what a file system does, and how paths name files, including a path trick attackers love.

**Time:** about 0:25

### 1.2 — What a file really is

**Show:** slide 1.2

**Say:** You think of a file as a document, a photo, a song. Underneath, a file is just a named sequence of bytes stored on a drive. That's the whole definition. A photo, a program, a video, a text note, all the same kind of thing to the computer: a string of bytes with a name. What makes one a photo and another a program is only how the bytes are arranged and how they're meant to be read, which is the lesson-1 idea applied to storage. Two consequences: any file can be examined as raw bytes with a hex dump, whatever its type, which is how reverse engineers and forensic analysts look inside files. And the "type" of a file isn't a deep property of the bytes; it's just a convention about how to read them, and it can be faked.

**Time:** about 0:50

### 1.3 — File systems

**Show:** slide 1.3

**Say:** A drive is just an enormous space for bytes, so something has to organize it, keep track of which bytes belong to which file, where each starts, what it's called, who may read it. That's the file system. You've met their names: NTFS on Windows, APFS on modern macOS, ext4 on Linux, FAT32 on USB sticks. Each is a different scheme, but they all do the same core jobs: keep an index of every file, track which parts of the drive are used and free, and store each file's metadata. And here's the crucial idea: a file's name and its bytes are stored separately. The file system keeps a record saying "this file lives in these locations" apart from the actual bytes. That separation sounds like a detail, but it's the key to understanding deletion and a lot of disk forensics.

**Time:** about 0:50

### 1.4 — Paths and the `..` trick

**Show:** slide 1.4

**Say:** Files are organized into directories, or folders, and directories contain other directories, forming a tree. To name a file's exact spot, you write a path: the directories leading to it, separated by slashes. On Linux and macOS, forward slashes from the root. On Windows, backslashes from a drive letter. A path from the very top is absolute; a path from where you are is relative. And two special names appear: a single dot means the current directory, and two dots means the parent, one level up. That two-dots is small but important in security. Because it means "go up a level," a carelessly handled path can be tricked into climbing out of where it should stay. An attacker who supplies a filename like dot-dot-slash-dot-dot-slash-etc-passwd may escape the intended folder and reach sensitive files. That's a real web attack called path traversal. The lesson: paths from a user are untrusted input, and dot-dot is the classic trick.

**Time:** about 0:55

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: a file is a named sequence of bytes, and its type is just interpretation. A file system indexes files, and crucially stores a file's name separately from its bytes. And paths name locations, where dot-dot means up a level, the path-traversal trick. Next, the information a file carries about itself, how to find its real type, and why deleting a file doesn't make it gone.

**Time:** about 0:25

---

## Video 2 — Metadata, Magic Bytes, and Deletion

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video: the metadata and permissions every file carries, how to find a file's real type with magic bytes even when the extension lies, and the forensics-critical fact that deleting a file usually doesn't destroy it.

**Time:** about 0:20

### 2.2 — Metadata and permissions

**Show:** slide 2.2

**Say:** Besides its bytes, every file carries metadata: data about the file, kept by the file system, its size, its timestamps, and its permissions. Permissions connect straight back to Security Fundamentals. On Linux and macOS, every file has permissions for three kinds of people, the owner, the group, and everyone else, and three actions, read, write, execute. The `ls -l` command shows them. Read the first column in groups: the first character is the type, then three for the owner, three for the group, three for everyone else. So `menu.txt` with `rw-`, `r--`, `---` can be read and written by its owner, read by its group, and not touched by anyone else, least privilege, enforced per file. And metadata matters hugely in forensics: timestamps build a timeline of what happened and when, like whether a file appeared right after a suspicious login.

**Time:** about 0:55

### 2.3 — Magic bytes: the extension lies

**Show:** slide 2.3

**Say:** How does a computer know a file is a PNG and not text? You might say the extension, dot png. But the extension is just part of the name, and anyone can change it, renaming a photo to dot txt doesn't change a single byte. So the extension can't be trusted. The real answer is inside the file: most formats begin with a few fixed bytes called magic bytes, a signature. A PNG always starts with `89 50 4e 47`, where the last three spell "PNG" in ASCII. In the demo, there it is at the very start, whatever the file's named. The `file` command identifies files this way, by content, so it correctly calls dot.png a PNG image by its bytes, not its name. This gap is a security goldmine: attackers hide malware by faking the extension, a file named invoice.pdf might really be a program, and file-upload filters that only check the extension are easily bypassed. Trust the content, not the name.

**Time:** about 0:55

### 2.4 — Delete vs really delete

**Show:** slide 2.4

**Say:** When you delete a file and empty the trash, is it gone? Usually not, and this is one of the most important ideas in forensics. Remember, the name-and-index and the bytes are stored separately. When you delete, the file system normally just removes the index entry and marks the space as free. The actual bytes are not erased, they sit on the drive exactly as before, until that space happens to be reused. It's like removing a book's card from the library catalogue but leaving the book on the shelf: the catalogue says the shelf is empty, but the book is still physically there. So deleted files can often be recovered, forensic tools scan for the leftover bytes, a technique called file carving, often using magic bytes to spot where files begin. And truly erasing data takes extra work: overwriting the bytes, encrypting the whole drive, or physically destroying it. One related idea: mounting is connecting a device's file system into the tree you browse, and forensics mounts a suspect's drive read-only, so the act of looking can't change the evidence.

**Time:** about 1:00

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: metadata, the permissions and timestamps, controls access and builds forensic timelines. Magic bytes reveal a file's real type, because the extension can lie, so trust the content. Deleting a file just removes its index entry, so the bytes remain and are often recoverable, while really erasing needs overwriting or encryption. And forensics always mounts drives read-only to preserve the original. Next lesson, we look at a special and important kind of file, the program, and how source code becomes something the CPU can actually run.

**Time:** about 0:35
