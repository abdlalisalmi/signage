"use server";

import { redirect } from "next/navigation";

export default async function Screens() {
  redirect(`/`); // Navigate to the new post page
}
