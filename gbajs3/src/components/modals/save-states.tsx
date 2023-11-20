import { Button, TextField } from '@mui/material';
import { useCallback, useContext, useEffect, useId, useState } from 'react';
import { useForm, type SubmitHandler } from 'react-hook-form';
import { BiError, BiPlus, BiTrash } from 'react-icons/bi';
import { styled, useTheme } from 'styled-components';
import { useLocalStorage } from 'usehooks-ts';

import { ModalBody } from './modal-body.tsx';
import { ModalFooter } from './modal-footer.tsx';
import { ModalHeader } from './modal-header.tsx';
import { EmulatorContext } from '../../context/emulator/emulator.tsx';
import { ModalContext } from '../../context/modal/modal.tsx';
import {
  EmbeddedProductTour,
  type TourSteps
} from '../product-tour/embedded-product-tour.tsx';
import { ErrorWithIcon } from '../shared/error-with-icon.tsx';
import { CenteredText } from '../shared/styled.tsx';

type InputProps = {
  saveStateSlot: number;
};

const LoadSaveStateButton = styled.button`
  padding: 0.5rem 0.5rem;
  width: 100%;
  color: ${({ theme }) => theme.blueCharcoal};
  background-color: ${({ theme }) => theme.pureWhite};
  border: none;
  text-align: left;

  &:hover {
    color: ${({ theme }) => theme.darkGrayBlue};
    background-color: ${({ theme }) => theme.aliceBlue1};
  }
`;

const StyledLi = styled.li`
  cursor: pointer;
  display: grid;
  grid-template-columns: auto 32px;
  gap: 10px;

  color: ${({ theme }) => theme.blueCharcoal};
  background-color: ${({ theme }) => theme.pureWhite};
  border: 1px solid rgba(0, 0, 0, 0.125);

  &:hover {
    color: ${({ theme }) => theme.darkGrayBlue};
    background-color: ${({ theme }) => theme.aliceBlue1};
  }
`;

const SaveStatesList = styled.ul`
  list-style-type: none;
  display: flex;
  flex-direction: column;
  margin: 0;
  padding: 0;

  & > ${StyledLi}:first-child {
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
  }

  & > ${StyledLi}:last-child {
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
  }

  & > ${StyledLi}:not(:first-child) {
    border-top-width: 0;
  }
`;

const StyledBiPlus = styled(BiPlus)`
  width: 25px;
  height: 25px;
`;

const StyledCiCircleRemove = styled(BiTrash)`
  height: 100%;
  width: 20px;
`;

const StyledForm = styled.form`
  display: flex;
  justify-content: space-between;
  gap: 16px;
  border-bottom: 1px solid ${({ theme }) => theme.pattensBlue};
  margin-bottom: 16px;
  padding-bottom: 16px;
`;

export const SaveStatesModal = () => {
  const theme = useTheme();
  const { setIsModalOpen } = useContext(ModalContext);
  const { emulator } = useContext(EmulatorContext);
  const [currentSaveStates, setCurrentSaveStates] = useState<
    string[] | undefined
  >();
  const [saveStateError, setSaveStateError] = useState<string | null>(null);
  const [currentSlot, setCurrentSlot] = useLocalStorage(
    'currentSaveStateSlot',
    0
  );
  const saveStatesFormId = useId();
  const saveStatesListId = useId();
  const addStateButtonId = useId();
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors }
  } = useForm<InputProps>({
    defaultValues: {
      saveStateSlot: currentSlot
    }
  });

  const refreshSaveStates = useCallback(() => {
    const saveStatesList = emulator
      ?.listSaveStates()
      ?.filter((ss) => ss !== '.' && ss !== '..');

    setCurrentSaveStates(saveStatesList);
  }, [emulator]);

  useEffect(() => {
    refreshSaveStates();
  }, [refreshSaveStates]);

  useEffect(() => {
    setValue('saveStateSlot', currentSlot);
  }, [currentSlot, setValue]);

  const incrementCurrentSlot = () => {
    setCurrentSlot((prevState) => prevState + 1);
  };

  const onSubmit: SubmitHandler<InputProps> = async (formData) => {
    setCurrentSlot(formData.saveStateSlot);
  };

  const tourSteps: TourSteps = [
    {
      content: (
        <p>
          Use this input and button to manually update the current save state
          slot in use.
        </p>
      ),
      placementBeacon: 'bottom-end',
      target: `#${CSS.escape(saveStatesFormId)}`
    },
    {
      content: (
        <p>
          Tap a row to load a save state, or use the trash can icon to delete a
          save state.
        </p>
      ),
      placementBeacon: 'bottom-end',
      target: `#${CSS.escape(saveStatesListId)}`
    },
    {
      content: (
        <p>
          Use the <i>plus</i> button to add a new save state. This will
          automatically increase the current save state number!
        </p>
      ),
      placementBeacon: 'bottom-end',
      target: `#${CSS.escape(addStateButtonId)}`
    }
  ];

  return (
    <>
      <ModalHeader title="Manage Save States" />
      <ModalBody>
        <StyledForm id={saveStatesFormId} onSubmit={handleSubmit(onSubmit)}>
          <TextField
            label="Current Save State Slot"
            type="number"
            InputLabelProps={{
              shrink: true
            }}
            size="small"
            error={!!errors?.saveStateSlot}
            helperText={errors?.saveStateSlot?.message}
            {...register('saveStateSlot', {
              required: { value: true, message: 'Slot is required' },
              min: { value: 0, message: 'Slot must be >= 0' },
              valueAsNumber: true
            })}
          />
          <Button
            form={saveStatesFormId}
            type="submit"
            variant="outlined"
            size="small"
          >
            Update Slot
          </Button>
        </StyledForm>

        <SaveStatesList id={saveStatesListId}>
          {currentSaveStates?.map?.((saveState: string, idx: number) => (
            <StyledLi key={`${saveState}_${idx}`}>
              <LoadSaveStateButton
                onClick={() => {
                  const ext = saveState.split('.').pop();
                  const slotString = ext?.replace('ss', '');
                  if (slotString) {
                    const slot = parseInt(slotString);
                    const hasLoadedSaveState = emulator?.loadSaveState(slot);
                    if (hasLoadedSaveState) {
                      setCurrentSlot(slot);
                      setSaveStateError(null);
                    } else {
                      setSaveStateError('Failed to load save state');
                    }
                  }
                }}
              >
                {saveState}
              </LoadSaveStateButton>
              <StyledCiCircleRemove
                onClick={() => {
                  const ext = saveState.split('.').pop();
                  const slotString = ext?.replace('ss', '');
                  if (slotString) {
                    const slot = parseInt(slotString);
                    emulator?.deleteSaveState(slot);
                    refreshSaveStates();
                  }
                }}
              />
            </StyledLi>
          ))}
          {!currentSaveStates?.length && (
            <li>
              <CenteredText>No save states</CenteredText>
            </li>
          )}
        </SaveStatesList>
        <StyledBiPlus
          id={addStateButtonId}
          onClick={() => {
            const hasCreatedSaveState = emulator?.createSaveState(
              currentSlot + 1
            );
            if (hasCreatedSaveState) {
              refreshSaveStates();
              incrementCurrentSlot();
              setSaveStateError(null);
            } else {
              setSaveStateError('Failed to create save state');
            }
          }}
        />
        {saveStateError && (
          <ErrorWithIcon
            icon={<BiError style={{ color: theme.errorRed }} />}
            text={saveStateError}
          />
        )}
      </ModalBody>
      <ModalFooter>
        <Button variant="outlined" onClick={() => setIsModalOpen(false)}>
          Close
        </Button>
      </ModalFooter>
      <EmbeddedProductTour
        steps={tourSteps}
        completedProductTourStepName="hasCompletedSaveStatesTour"
      />
    </>
  );
};
