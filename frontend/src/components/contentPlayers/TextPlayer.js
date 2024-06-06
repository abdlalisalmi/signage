"use client";
import { useEditor, EditorContent } from "@tiptap/react";
import StarterKit from "@tiptap/starter-kit";
import CircularProgressTimer from "./CircularProgressTimer";

export default function TextPlayer({ content, switchContent }) {
  const editor = useEditor({
    extensions: [StarterKit],
    content: content.text,
    editable: false,
  });

  return (
    <main className="min-h-screen flex items-center justify-center">
      <div className="w-4/5">
        <EditorContent editor={editor} />
      </div>
      <div className="absolute bottom-4 right-4">
        <CircularProgressTimer
          duration={content.duration}
          callback={switchContent}
        />
      </div>
    </main>
  );
}
