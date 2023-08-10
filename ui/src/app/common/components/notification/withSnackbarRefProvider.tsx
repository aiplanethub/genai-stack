import React from "react";
import dynamic from "next/dynamic";

const SnackbarRefProvider = dynamic(() => import("./SnackbarRefProvider"), {
  ssr: false,
});

function withSnackbarRefProvider<T extends any>(
  WrappedComponent: React.ComponentType<T>
) {
  // Try to create a nice displayName for React Dev Tools.
  const displayName =
    WrappedComponent.displayName || WrappedComponent.name || "Component";

  // Creating the inner component. The calculated Props type here is the where the magic happens.
  const ComponentWithSnackbarRefProvider = (props?: any) => {
    return (
      <SnackbarRefProvider>
        <WrappedComponent {...(props || {})} />
      </SnackbarRefProvider>
    );
  };

  ComponentWithSnackbarRefProvider.displayName = `withSnackbarRefProvider(${displayName})`;

  return ComponentWithSnackbarRefProvider;
}

export default withSnackbarRefProvider;
