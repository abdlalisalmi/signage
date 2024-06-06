"use client";

import CustomLoader from "@/components/CustomLoader";

const ErrorComponent = ({ message, code }) => {
  return (
    <main className="flex items-center justify-center min-h-screen bg-white dark:bg-black">
      <div className="text-center">
        <h1 className="border-r pr-6 mr-6 text-3xl font-medium inline-block text-black dark:text-white border-gray-300 dark:border-gray-600">
          {code}
        </h1>
        <div className="inline-block">
          <h2 className="text-base font-normal text-black dark:text-white">
            {message || "An unexpected error occurred."}
          </h2>
        </div>
      </div>
    </main>
  );
};

export default function Layout({ children, loading, error }) {
  if (loading) {
    return (
      <main className="flex min-h-screen flex-col items-center justify-center">
        <CustomLoader />
      </main>
    );
  }

  if (error) {
    if (!error.response) {
      return <ErrorComponent code={500} message="An error occurred" />;
    } else if (error.response) {
      return (
        <ErrorComponent
          code={error.response.status}
          message={error.response?.data?.detail}
        />
      );
    }
  }
  return <div>{children}</div>;
}
