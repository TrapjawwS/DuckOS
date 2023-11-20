import { Toaster } from 'react-hot-toast';
import { ThemeProvider } from 'styled-components';

import './App.css';
import { UserControls } from './components/controls/user-controls.tsx';
import { ModalContainer } from './components/modals/modal-container.tsx';
import { NavigationMenu } from './components/navigation-menu/navigation-menu.tsx';
import { ProductTourIntro } from './components/product-tour/product-tour-intro.tsx';
import { Screen } from './components/screen/screen.tsx';
import { AuthProvider } from './context/auth/auth.tsx';
import { EmulatorProvider } from './context/emulator/emulator.tsx';
import { ModalProvider } from './context/modal/modal.tsx';
import { GbaDarkTheme } from './context/theme/theme.tsx';

export const App = () => {
  return (
    <ThemeProvider theme={GbaDarkTheme}>
      <ProductTourIntro />
      <Toaster />
      <AuthProvider>
        <EmulatorProvider>
          <ModalProvider>
            <NavigationMenu />
            <Screen />
            <UserControls />
            <ModalContainer />
          </ModalProvider>
        </EmulatorProvider>
      </AuthProvider>
    </ThemeProvider>
  );
};
