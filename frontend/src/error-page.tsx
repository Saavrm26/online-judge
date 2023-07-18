import { useRouteError } from "react-router-dom";

export default function ErrorPage() {
  type ErrorResponse = {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    [key: string]: any;
    statusText?: string;
    message?: string;
  };

  const error = useRouteError() as ErrorResponse;

  console.error(error);
  // let message = "";
  // if (error !== null) {
  //   if (error.statusText != undefined) message;
  // }
  return (
    <div id="error-page">
      <h1>Oops!</h1>
      <p>Sorry, an unexpected error has occurred.</p>
      <p>
        <i>{error.statusText || error.message}</i>
      </p>
    </div>
  );
}
